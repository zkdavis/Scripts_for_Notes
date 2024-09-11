import plotly.figure_factory as ff
import plotly.graph_objects as go
import numpy as np
from pathlib import Path

cur_dir = Path(__file__).resolve().parent
output_dir = cur_dir / "output"


def test_plot_quiver():
    x,y = np.meshgrid(np.arange(0, 2, .2), np.arange(0, 2, .2))
    u = np.cos(x)*y
    v = np.sin(x)*y
    fig = ff.create_quiver(x, y, u, v)
    fig.write_html(str(output_dir / "test_plot_quiver.html"))
    fig.show()


def test_plot_streamline():
    x = np.linspace(-3, 3, 100)
    y = np.linspace(-3, 3, 100)
    Y, X = np.meshgrid(x, y)
    u = -1 - X ** 2 + Y
    v = 1 + X - Y ** 2
    fig = ff.create_streamline(x, y, u, v, arrow_scale=.1)

    fig.write_html(str(output_dir / "test_plot_streamline.html"))
    fig.show()

def test_slider():
    fig = go.Figure()

    # Add traces, one for each slider step
    for step in np.arange(0, 5, 0.1):
        fig.add_trace(
            go.Scatter(
                visible=False,
                line=dict(color="#00CED1", width=6),
                name="𝜈 = " + str(step),
                x=np.arange(0, 10, 0.01),
                y=np.sin(step * np.arange(0, 10, 0.01))))

    # Make 10th trace visible
    fig.data[10].visible = True

    # Create and add slider
    steps = []
    for i in range(len(fig.data)):
        step = dict(
            method="update",
            args=[{"visible": [False] * len(fig.data)},
                  {"title": "Slider switched to $j_z$: " + str(i)}],  # layout attribute
        )
        step["args"][0]["visible"][i] = True  # Toggle i'th trace to "visible"
        steps.append(step)

    sliders = [dict(
        active=10,
        currentvalue={"prefix": "Frequency: "},
        pad={"t": 50},
        steps=steps
    )]

    fig.update_layout(
        sliders=sliders
    )

    fig.write_html(str(output_dir / "test_plot_slider.html"))
    fig.show()


def null_point():
    fig = go.Figure()
    x = np.linspace(-3, 3, 100)
    y = np.linspace(-3, 3, 100)
    X, Y = np.meshgrid(x, y, indexing='ij')
    j_values = np.linspace(-4, 4, 49)
    active_first = np.argmin(np.abs(j_values))
    j_thresh = 1
    for jz in j_values:
        Bx = (X / 2) * (j_thresh + jz)
        By = (Y / 2) * (j_thresh - jz)
        fig.add_trace(
            ff.create_streamline(
                visible=False,
                name="$j_z$ = " + str(jz),
                x=x,
                y=y,
                u=Bx,
                v=By,
                density=1
            ).data[0]
        )

    fig.update_layout(
        title_text=r"$\text{Magnetic Null Point for }j_z=" + str(np.round(j_values[active_first], 2)) + r"\text{ } j_{thresh}=1$",
        title_x=0.5,
        title_font=dict(size=30),  # Increase title size
        xaxis=dict(
            tickfont=dict(size=18),  # Larger x-axis tick labels
            range=[-3, 3]  # Set x-axis range
        ),
        yaxis=dict(
            tickfont=dict(size=18),  # Larger y-axis tick labels
            range=[-3, 3]  # Set y-axis range
        )
    )
    fig.data[active_first].visible = True

    steps = []
    for i in range(len(fig.data)):
        step = dict(
            method="update",
            label=str(np.round(j_values[i], 2)),
            args=[{"visible": [False] * len(fig.data)},
                  {"title": r"$\text{Magnetic Null Point for }j_z=" + str(np.round(j_values[i], 2)) + r"\text{ } j_{thresh}=1$"}],
        )
        step["args"][0]["visible"][i] = True
        steps.append(step)

    sliders = [dict(
        active=active_first,
        currentvalue={"visible": False},
        pad={"t": 50},
        steps=steps,
        font=dict(size=18)  # Increase slider tick size
    )]

    fig.update_layout(
        sliders=sliders
    )

    fig.write_html(str(output_dir / "magnetic_null_point.html"))
    fig.show()


if __name__ == "__main__":
    # test_plot_quiver()
    # test_plot_streamline()
    null_point()