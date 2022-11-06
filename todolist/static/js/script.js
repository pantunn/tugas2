function submitTodo() {
    fetch("add/",{
        method:"POST",
        body: new FormData(document.querySelector('#forms'))
    }).then(showTodo)
    document.getElementById("/forms").reset();
    return false
}

function showTodo(){
    let str="";
    $.ajax({
        url: "json",
        type: "GET",
        dataType: "json",
        success: function(data) {
            data.forEach(e => {
                str+= `
                
                    <div class="card" style="width: 150px; margin: 5px; background-color: rgb(193, 167, 147);">
                        <div class="card-body">
                            <div style="display: flex; flex-direction: row;">
                            <h1 class="card-title">${e.fields.title}</h1>
                            </div>
                            <p class="card-text">${e.fields.description}</p>
                        </div>
                    </div>
               `
                ;
            });
            $('#accordionPanelsStayOpenExample').html(str);
            
            
        }

    })
};
document.getElementById("submits").onclick = submitTodo