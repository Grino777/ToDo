function search () {
    let input = document.getElementById("search_form");
    let filter = input.value.toUpperCase();
    let ul = document.getElementById("tasks_list");
    let li = ul.getElementsByTagName("li");

    for (let i = 0; i < li.length; i++) {
        if (li[i].className === 'unfinished__task__title' | li[i].className === 'finished__task__title') {
            continue
        } else {
            let a = li[i].getElementsByTagName("a")[0];
            if (a.innerHTML.toUpperCase().indexOf(filter) > -1) {
                li[i].style.display = "";
        } else {
            li[i].style.display = "none";
        }}}}

document.addEventListener('keyup', search);