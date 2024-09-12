import numpy as np
import plotly.graph_objects as go
from pathlib import Path

cur_dir = Path(__file__).resolve().parent
output_dir = cur_dir / "output"

def one_point_one_z():
    x = np.linspace(-5, 5, 200)
    y = np.linspace(-5, 5, 200)
    X, Y = np.meshgrid(x, y)

    def calculate_z(c):
        return np.sqrt(X**2 + Y**2 - c)

    c = 0
    Z = calculate_z(c)

    fig = go.Figure(data=[go.Surface(z=Z, x=X, y=Y)])

    fig.update_layout(
        title='Surface Plot of x^2 + y^2 - z^2 = c',
        scene=dict(
            xaxis_title='X',
            yaxis_title='Y',
            zaxis_title='Z'
        ),
        sliders=[{
            'active': 0,
            'currentvalue': {"prefix": "c: "},
            'pad': {"t": 50},
            'steps': [
                {
                    'method': 'update',
                    'label': str(round(c, 2)),
                    'args': [
                        {'z': [calculate_z(c)]},
                        {'title': f'Surface Plot of x^2 + y^2 - z^2 = {round(c, 2)}'}
                    ]
                } for c in np.linspace(-1, 1, 51)
            ]
        }]
    )

    fig.write_html(str(output_dir / "one_point_one_z.html"))
    fig.show()


def one_point_one_x():
    z = np.linspace(-5, 5, 200)
    y = np.linspace(-5, 5, 200)
    Y, Z = np.meshgrid(y, z)

    def calculate_x(c):
        return np.sqrt(c - Y ** 2 + Z ** 2)

    c = 0
    X = calculate_x(c)

    fig = go.Figure(data=[go.Surface(z=Z, x=X, y=Y)])

    fig.update_layout(
        title='Surface Plot of x^2 + y^2 - z^2 = c',
        scene=dict(
            xaxis_title='X',
            yaxis_title='Y',
            zaxis_title='Z'
        ),
        sliders=[{
            'active': 0,
            'currentvalue': {"prefix": "c: "},
            'pad': {"t": 50},
            'steps': [
                {
                    'method': 'update',
                    'label': str(round(c, 2)),
                    'args': [
                        {'x': [calculate_x(c)]},
                        {'title': f'Surface Plot of x^2 + y^2 - z^2 = {round(c, 2)}'}
                    ]
                } for c in np.linspace(-1, 1, 51)
            ]
        }]
    )
    fig.write_html(str(output_dir / "one_point_one_x.html"))
    fig.show()

def one_point_one_y():
    z = np.linspace(-5, 5, 200)
    x = np.linspace(-5, 5, 200)
    X, Z = np.meshgrid(x, z)

    def calculate_y(c):
        return np.sqrt(c - X ** 2 + Z ** 2)

    c = 0
    Y = calculate_y(c)

    fig = go.Figure(data=[go.Surface(z=Z, x=X, y=Y)])

    fig.update_layout(
        title='Surface Plot of x^2 + y^2 - z^2 = c',
        scene=dict(
            xaxis_title='X',
            yaxis_title='Y',
            zaxis_title='Z'
        ),
        sliders=[{
            'active': 0,
            'currentvalue': {"prefix": "c: "},
            'pad': {"t": 50},
            'steps': [
                {
                    'method': 'update',
                    'label': str(round(c, 2)),
                    'args': [
                        {'y': [calculate_y(c)]},
                        {'title': f'Surface Plot of x^2 + y^2 - z^2 = {round(c, 2)}'}
                    ]
                } for c in np.linspace(-1, 1, 51)
            ]
        }]
    )

    fig.write_html(str(output_dir / "one_point_one_y.html"))
    fig.show()

if __name__ == "__main__":
    one_point_one_x()
    one_point_one_y()
    one_point_one_z()