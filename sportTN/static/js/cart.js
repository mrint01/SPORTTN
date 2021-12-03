var updateBtns = document.getElementsByClassName('update-cart')


for (i = 0; i < updateBtns.length; i++) {
	updateBtns[i].addEventListener('click', function(){
		var productId = this.dataset.product
		var action = this.dataset.action
		//var valeur = this.dataset.val
		
		if ( document.getElementById('valeur') == null){
			var valeur = "1"
		}else{
			var valeur = document.getElementById('valeur').value
		}

		
		console.log('productId:', productId, 'Action:', action)
		console.log('USER:', user)
		console.log(valeur)
		

		if (user == 'AnonymousUser'){
            console.log('User not found')

			//addCookieItem(productId, action)
		}else{
			updateUserOrder(productId, action,valeur)
		}
	})
}

function updateUserOrder(productId, action,valeur){
	console.log('User is authenticated, sending data...')

		var url = '/cart/update_item'

		fetch(url, {
			method:'POST',
			headers:{
				'Content-Type':'application/json',
				'X-CSRFToken':csrftoken,
			}, 
			body:JSON.stringify({'productId':productId, 'action':action,"valeur":valeur})
            
		})
		.then((response) => {
		   return response.json();
		})
		.then((data) => {
            console.log('data' , data)
		    location.reload()
		});
}
/*
function addCookieItem(productId, action){
	console.log('User is not authenticated')

	if (action == 'add'){
		if (cart[productId] == undefined){
		cart[productId] = {'quantity':1}

		}else{
			cart[productId]['quantity'] += 1
		}
	}

	if (action == 'remove'){
		cart[productId]['quantity'] -= 1

		if (cart[productId]['quantity'] <= 0){
			console.log('Item should be deleted')
			delete cart[productId];
		}
	}
	console.log('CART:', cart)
	document.cookie ='cart=' + JSON.stringify(cart) + ";domain=;path=/"
	
	location.reload()
}*/