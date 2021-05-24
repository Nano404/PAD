function check(){

    if (document.cookie.split(';').some((item) => item.includes('isAdmin=True'))) {
        window.location.href = "/adminindex.html";
    }
}

<button onclick="check()">Admin</button>

if (document.cookie.indexOf('isAdmin') !=-1) {
} else {
  document.cookie = "isAdmin=False";
}
