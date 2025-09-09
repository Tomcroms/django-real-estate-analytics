function displayStartBtn() {

    index_title = document.getElementById("index_title");
    index_title.style.display = "none";

    second_title = document.getElementById("second_title");
    second_title.style.display = "none";

    startBtn = document.getElementById("start_btn");
    startBtn.style.width = "100%";
    startBtn.classList.remove("start_btn_hover")
    startBtn.removeAttribute("onlick");

    graphContainer = document.getElementById("graph_container");
    graphContainer.style.display = "flex";

    document.getElementById("start_now_text").style.display = "none";
}

function userWantsOverview(){
    document.getElementById("overview").style.backgroundColor = "rgba(255, 255, 255, 0.15)";
    window.location.href = "/graph/overview/";
}

function userWantsType(){
    document.getElementById("type").style.backgroundColor = "rgba(255, 255, 255, 0.15)";
    window.location.href = "/graph/";
}

function userWantsMutation(){
    document.getElementById("mutation").style.backgroundColor = "rgba(255, 255, 255, 0.15)";
    window.location.href = "/graph/";
}

function userWantsEvolution(){
    document.getElementById("evolution").style.backgroundColor = "rgba(255, 255, 255, 0.15)";
    window.location.href = "/graph/";
}

function userWantsCovid(){
    document.getElementById("covid").style.backgroundColor = "rgba(255, 255, 255, 0.15)";
    window.location.href = "/graph/";
}
