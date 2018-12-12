port module Main exposing (main)
import Browser

import Browser.Events exposing (onAnimationFrameDelta, onResize)
import Game.Resources as Resources exposing (Resources)
import Game.TwoD as Game
import Game.TwoD.Render as Render exposing (Renderable)
import Html exposing (div, Html)
import Html.Attributes as Attr
import Keyboard
import Models exposing (..)
import Update exposing (update)


render : Model -> List Renderable
render ({ resources, camera } as model) =
    let
        players = case model.state of
            InGame gameState ->
                gameState.players
            other -> []
    in
    List.concat
        [ renderBackground resources
        , List.map (renderPlayer resources) players
        ]


renderBackground : Resources -> List Renderable
renderBackground resources =
    [ Render.parallaxScroll
        { z = -0.99
        , texture = Resources.getTexture "images/cloud_bg.png" resources
        , tileWH = ( 1, 1 )
        , scrollSpeed = ( 0.25, 0.25 )
        }
    , Render.parallaxScroll
        { z = -0.98
        , texture = Resources.getTexture "images/cloud_bg.png" resources
        , tileWH = ( 1.4, 1.4 )
        , scrollSpeed = ( 0.5, 0.5 )
        }
    ]


renderPlayer : Resources -> Player -> Renderable
renderPlayer resources { x, y } =
    Render.sprite
        { position = ( x, y )
        , size = ( 0.8, 0.8 )
        , texture = Resources.getTexture "images/player-man.png" resources
        }


view : Model -> Html msg
view ({ time, screen } as model) =
    div [ Attr.style "overflow" "hidden", Attr.style "width" "100%", Attr.style "height" "100%" ]
        [ Game.render
            { camera = model.camera
            , time = time
            , size = screen
            }
            (render model)
        ]


main : Program () Model Msg
main =
    Browser.element
        { update = update
        , init = init
        , view = view
        , subscriptions = subs
        }

-- JavaScript usage: app.ports.websocketIn.send(response);
port websocketIn : (String -> msg) -> Sub msg
-- JavaScript usage: app.ports.websocketOut.subscribe(handler);
port websocketOut : String -> Cmd msg

subs : Model -> Sub Msg
subs model =
    Sub.batch
        [ websocketIn WebsocketIn
        , onResize ScreenSize
        , Sub.map Keys Keyboard.subscriptions
        , onAnimationFrameDelta ((\dt -> dt / 1000) >> Tick)]