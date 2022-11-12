function book() {
    // (A1) PREVENT MULTIPLE SUBMIT
    document.getElementById("bookGo").disable = true;
    // (A2) COLLECT FORM DATA
    let data = new FormData(document.getElementById("bookForm"));
//send
    fetch("/book", { method:"POST", body:data})
    .then((res) => {
        if (res.status==200) {location.href = "/thank"; }
        else { alert("Error"); }
    })
    .catch((err) => { alert("Error"); });
    return false;
}

//load
window.onload = () => {
    let datepick =  document.getElementsByName("date")[0];
    datepick.min = new Date().toISOString().split("T")[0];
//form
    document.getElementById("bookGo").disabled = false;

};
