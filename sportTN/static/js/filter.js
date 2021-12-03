function searchProduct(){

   const input =  document.getElementById('filter').value.toUpperCase();
   
   const cardContainer = document.getElementById('cards');

   const cards = cardContainer.getElementsByClassName('card');

   for(let i =0; i<cards.length; i++){
       let title = cards[i].querySelector(".description h1");
       
       if(title.innerText.toUpperCase().indexOf(input) > -1){
           cards[i].style.display ="";
       }else{
        cards[i].style.display ="none";
       }
   }

}
