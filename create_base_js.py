import os

# Create the directory structure
os.makedirs("techshop/assets/css", exist_ok=True)
os.makedirs("techshop/assets/js", exist_ok=True)

# Create the base HTML file with linked CSS and JS
index_html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Techshop</title>
    <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
    <header>
        <h1>Techshop</h1>
        <nav>
            <button id="nav-toggle">☰ Menu</button>
            <ul id="nav-menu">
                <li><a href="#">Home</a></li>
                <li><a href="#">Projects</a></li>
                <li><a href="#">Collaborate</a></li>
                <li><a href="#">Forum</a></li>
                <li><a href="#">Shop</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <h2>Welcome to Techshop</h2>
        <p>Your hub for AI innovation, collaboration, and tools.</p>
    </main>
    <footer>
        <p>&copy; 2024 Techshop. All rights reserved.</p>
    </footer>
    <script src="assets/js/main.js"></script>
</body>
</html>
"""

# Create the CSS file
style_css_content = """body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
}
header {
    background-color: #222;
    color: white;
    padding: 1rem;
}
nav {
    display: flex;
    flex-direction: column;
}
#nav-toggle {
    background: none;
    border: none;
    color: white;
    font-size: 1.5rem;
    display: none;
}
#nav-menu {
    list-style: none;
    padding: 0;
    margin: 0;
    display: flex;
    gap: 1rem;
}
#nav-menu li a {
    color: white;
    text-decoration: none;
}
footer {
    background-color: #f0f0f0;
    text-align: center;
    padding: 1rem;
    margin-top: 2rem;
}
@media (max-width: 600px) {
    #nav-toggle {
        display: block;
    }
    #nav-menu {
        display: none;
        flex-direction: column;
    }
    #nav-menu.active {
        display: flex;
    }
}
"""

# Create the JavaScript file
main_js_content = """document.addEventListener("DOMContentLoaded", function () {
    alert("Welcome to Techshop!");

    const navToggle = document.getElementById("nav-toggle");
    const navMenu = document.getElementById("nav-menu");

    navToggle.addEventListener("click", function () {
        navMenu.classList.toggle("active");
    });
});
"""

# Write the files
with open("techshop/index.html", "w", encoding="utf-8") as f:
    f.write(index_html_content)

with open("techshop/assets/css/style.css", "w") as f:
    f.write(style_css_content)

with open("techshop/assets/js/main.js", "w") as f:
    f.write(main_js_content)

print("Base HTML, CSS, and JavaScript files for Techshop have been created.")

