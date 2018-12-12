module Models exposing (..)

import Array exposing (Array)
import Browser.Dom exposing (getViewport)
import Game.Resources as Resources exposing (Resources)
import Game.TwoD.Camera as Camera exposing (Camera)
import Keyboard
import Task



type Msg
    = ScreenSize Int Int
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
