function check(){

    if (document.cookie.split(';').some((item) => item.includes('isAdmin=True'))) {
        window.location.href = "/adminindex.html";
    }
}

<button onclick="check()">Admin</button>