import dash_core_components as dcc
import dash_html_components as html

# isort: off
from maindash import spectrum_fig, waterfall_fig

# isort: on
layout = html.Div(
    [
        html.Div(
            [
                html.Center([
                    html.Div(
                        [
                            html.Div("", className="dummy-body"),
                            html.Div("Уровень мощности:", id="label_daq_power_level_2", className="field-label"),
                            html.Div("-", id="body_daq_power_level_2", className="field-body-2"),
                            html.Div("", className="dummy-body"),

                            html.Div("Буфер:", id="label_history", className="field-body-2"),
                            html.Div("-", id="body_history", className="field-body"),
                            html.Button("Проигрывать", id="play-history-btn", n_clicks=0, className="play-btn"),
                            html.Button("Записывать", id="record-history-btn", n_clicks=0, className="record-btn"),
                        ],
                        className="row-block",
                    ),]
                ),
                dcc.Graph(
                    id="spectrum-graph",
                    style={"width": "100%", "height": "45%"},
                    figure=spectrum_fig,  # fig_dummy #spectrum_fig #fig_dummy
                ),
                dcc.Graph(
                    id="waterfall-graph",
                    style={"width": "100%", "height": "65%"},
                    figure=waterfall_fig,  # waterfall fig remains unchanged always due to slow speed to update entire graph #fig_dummy #spectrum_fig #fig_dummy
                ),
            ],
            style={"width": "100%", "height": "80vh"},
        ),
    ]
)
