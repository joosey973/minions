from flask import Flask, render_template

app = Flask(__name__)


@app.route("/carousel")
def carousel():
    return f'''<!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8" />
                    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
                    <link
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"
                    rel="stylesheet"
                    />
                    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
                    <title>Пейзажи Миньонов</title>
                </head>
                <body>
                    <header>
                    <nav
                        class="navbar navbar-light"
                        style="display: flex; justify-content: center"
                    >
                        <h2>Пейзажи Миньонов</h2>
                    </nav>
                    </header>
                    <main
                    role="main"
                    class="container mt-5"
                    style="display: flex; justify-content: center"
                    >
                    <!-- Carousel -->
                    <div class="carousel slide" data-bs-ride="carousel" id="demo">
                        <!-- Indicators/dots -->
                        <div class="carousel-indicators">
                        <button
                            type="button"
                            data-bs-target="#demo"
                            data-bs-slide-to="0"
                            class="active"
                        ></button>
                        <button
                            type="button"
                            data-bs-target="#demo"
                            data-bs-slide-to="1"
                        ></button>
                        <button
                            type="button"
                            data-bs-target="#demo"
                            data-bs-slide-to="2"
                        ></button>
                        </div>
                        <!-- The slideshow/carousel -->
                        <div class="carousel-inner">
                        <div class="carousel-item active">
                            <img src="/static/img/1.png" alt="" />
                        </div>
                        <div class="carousel-item">
                            <img src="/static/img/2.png" alt="" />
                        </div>
                        <div class="carousel-item">
                            <img src="/static/img/3.png" alt="" />
                        </div>
                        </div>
                        <!-- Left and right controls/icons -->
                        <button
                        class="carousel-control-prev btn btn-dark"
                        type="button"
                        data-bs-target="#demo"
                        data-bs-slide="prev"
                        >
                        <span class="carousel-control-prev-icon"></span>
                        </button>
                        <button
                        class="carousel-control-next btn btn-dark"
                        type="button"
                        data-bs-target="#demo"
                        data-bs-slide="next"
                        >
                        <span class="carousel-control-next-icon"></span>
                        </button>
                    </div>
                    </main>
                </body>
                </html>
                '''


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080)
