function uploadPDF(){

    document.getElementById("tagcloud").innerHTML = "";
    document.getElementById("error").innerHTML = "";
    document.getElementById("submit-btn").disabled = true;
    document.getElementById("loader").style.display = "block";

    var form = $('#pdf_form')[0];
    var formData = new FormData(form);
    $.ajax({
        url : '/tagcloud/',
        type : 'POST',
        data: formData,
        cache: false,
        processData: false,
        contentType: false,
        success : function(response) {
            document.getElementById("loader").style.display = "none";
            document.getElementById("submit-btn").disabled = false;
            var html = '<img src=data:image/png;base64,'+response+' alt="">';
            document.getElementById("tagcloud").innerHTML = html;
        },
        error:function(e){
          document.getElementById("loader").style.display = "none";
          document.getElementById("submit-btn").disabled = false;
          document.getElementById("error").innerHTML = e.responseText;
        }
    });
}

function clr(){
  document.getElementById("error").innerHTML = "";
  document.getElementById("pdf").value = "";
}
