module Update exposing (update)

import Array
import Game.Resources as Resources exposing (Resources)
import Game.TwoD.Camera as Camera
import Keyboard
import Keyboard.Arrows
import Models exposing (Direction(..), Input, Player, Bullet, Model, GameState(..), GameBoard, Msg(..))


updatePlayer: Float -> Player -> Player
updatePlayer dt player =
    let
        faceX = Maybe.withDefault 0 (Array.get 0 player.face)
        faceY = Maybe.withDefault 0 (Array.get 1 player.face)
    in
    { player
      | x = player.x + player.speed * faceX
      , y = player.y + player.speed * faceY
    }

tick: Float -> GameState -> GameState
tick dt state =
    case state of
        InGame board ->
            InGame { board | players = List.map (updatePlayer dt) board.players }
        other -> other

update : Msg -> Model -> ( Model, Cmd Msg )
update msg model =
    case msg of
        ScreenSize width height ->
            ( { model | screen = ( width, height ) }
            , Cmd.none
            )

        Tick dt ->
            ( { model
                | state = (tick dt model.state)
                , time = dt + model.time
              }
            , Cmd.none
            )

        Resources rMsg ->
            ( { model | resources = Resources.update rMsg model.resources }
            , Cmd.none
            )

        Keys keyMsg ->
            let
                keys =
                    Keyboard.update keyMsg model.keys
            in
            ( { model | keys = keys }, Cmd.none )


-- tick : Float -> List Keyboard.Key -> Mario -> Mario
-- tick dt keys guy =
--     let
--         arrows =
--             Keyboard.Arrows.arrows keys
--     in
--     guy
--         |> gravity dt
--         |> jump arrows
--         |> walk arrows
--         |> physics dt
--

