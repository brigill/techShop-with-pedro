import os

# Define the directory structure
dirs = [
    "techshop",
    "techshop/assets",
    "techshop/assets/css",
    "techshop/assets/js"
]

# Create directories
for d in dirs:
    os.makedirs(d, exist_ok=True)

# Define base HTML content for index.html
index_html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Techshop - Home</title>
    <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
    <header>
        <h1>Techshop</h1>
        <nav>
            <ul>
                <li><a href="index.html">Home</a></li>
                <li><a href="projects/index.html">Projects</a></li>
                <li><a href="collaborate/index.html">Collaborate</a></li>
                <li><a href="forum/index.html">Forum</a></li>
                <li><a href="shop/index.html">Shop</a></li>
                <li><a href="resources/index.html">Resources</a></li>
                <li><a href="blog/index.html">Blog</a></li>
                <li><a href="about.html">About</a></li>
                <li><a href="account/login.html">Login</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <section>
            <h2>Welcome to Techshop</h2>
            <p>Your hub for AI innovation, collaboration, and tools.</p>
        </section>
    </main>
    <footer>
        <p>&copy; 2024 Techshop. All rights reserved.</p>
    </footer>
</body>
</html>
"""

# Define base CSS content for style.css
style_css_content = """/* Global Styles */
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    background: #f4f4f4;
    color: #333;
}

header {
    background: #222;
    color: #fff;
    padding: 1em 0;
    text-align: center;
}

header h1 {
    margin: 0;
}

nav ul {
    list-style: none;
    padding: 0;
    display: flex;
    justify-content: center;
    background: #333;
    margin: 0;
}

nav ul li {
    margin: 0;
}

nav ul li a {
    display: block;
    padding: 1em;
    color: #fff;
    text-decoration: none;
}

nav ul li a:hover {
    background: #555;
}

main {
    padding: 2em;
    background: #fff;
}

footer {
    text-align: center;
    padding: 1em;
    background: #222;
    color: #fff;
}
"""

# Write the HTML and CSS files
with open("techshop/index.html", "w") as f:
    f.write(index_html_content)

with open("techshop/assets/css/style.css", "w") as f:
    f.write(style_css_content)

print("Base HTML and CSS files have been generated in the 'techshop' directory.")

