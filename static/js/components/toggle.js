toggle = document.getElementById("toggle");
list = document.getElementById("list");
close_element = document.getElementById("close");
toggle.onclick = () => {

    document.getElementById("header-div").classList.toggle("hidden");
    list.classList.toggle("hidden");
    close_element.classList.toggle("hidden");
}
