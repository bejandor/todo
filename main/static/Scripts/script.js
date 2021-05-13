
function change_text(){
  let checkbox = document.getElementById("checkbox")
  let text = document.getElementsByClassName("todo_item")[0]
 
  if(checkbox.checked){
    text.style ="text-decoration:underline"

  }
  else{
      text.style ="text-decoration:none"
     
  }

}