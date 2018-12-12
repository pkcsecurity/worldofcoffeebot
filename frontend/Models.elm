module Models exposing (..)

import Array exposing (Array)
import Browser.Dom exposing (getViewport)
import Game.Resources as Resources exposing (Resources)
import Game.TwoD.Camera as Camera exposing (Camera)
import Keyboard
import Task
import Json.Decode as D
import Json.Encode as E



type Msg
    = Change String
    | Submit String
    | WebsocketIn String
    | ScreenSize Int Int
    | Tick Float
    | Resources Resources.Msg
    | Keys Keyboard.Msg

type alias Model =
    { state: GameState
    , resources : Resources
    , keys : List Keyboard.Key
    , time : Float
    , screen : ( Int, Int )
    , camera : Camera
    }

type GameState
    = StartScreen
    | InGame GameBoard
    | Died


boardDecoder : D.Decoder GameBoard
boardDecoder =
  D.map3
    GameBoard
    (D.field "pid" D.int)
    (D.field "players" (D.list playerDecoder))
    (D.field "bullets" (D.list bulletDecoder))


decoder : D.Decoder GameBoard
decoder =
  D.map3 GameBoard
    (D.field "name" D.string)
    (D.field "percent" D.float)
    (D.field "per100k" D.float)


type alias GameBoard =
    { pid: Int
    , players: List Player
    , bullets: List Bullet
    }

type alias Bullet =
    { x: Float
    , y: Float
    , speed: Float
    , face: Array Float
    }

type alias Player =
    { pid: Int
    , x: Float
    , y: Float
    , speed: Float
    , face: Array Float
    , move: Array Float
    , attacking: Bool
    , radius: Int
    , life: Int
    , character: Int
    }


type Direction
    = Left
    | Right


init : () -> ( Model, Cmd Msg )
init _ =
    ( { state = StartScreen
      , resources = Resources.init
      , keys = []
      , time = 0
      , screen = ( 800, 600 )
      , camera = Camera.fixedWidth 8 ( 0, 0 )
      }
    , Cmd.batch
        [ Cmd.map Resources (Resources.loadTextures [ "images/guy.png", "images/grass.png", "images/cloud_bg.png" ])
        , Task.perform (\{ viewport } -> ScreenSize (round viewport.width) (round viewport.height)) getViewport
        ]
    )


type alias Input =
    { x : Int, y : Int }
