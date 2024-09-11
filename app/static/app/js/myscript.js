$('#slider1, #slider2, #slider3').owlCarousel({
    loop: true,
    margin: 20,
    responsiveClass: true,
    responsive: {
        0: {
            items: 1,
            nav: false,
            autoplay: true,
        },
        600: {
            items: 3,
            nav: true,
            autoplay: true,
        },
        1000: {
            items: 5,
            nav: true,
            loop: true,
            autoplay: true,
        }
    }
})
$('.plus-cart').click(function () {
    var id=$(this).attr('pid').toString();
    var eml=this.parentNode.children[2]
    var price=document.getElementById('taamount')
    var minu=document.getElementById('minnu')
    var ajit=document.getElementById('ajit')
    console.log(minu)
    console.log(eml)
    console.log(id)
    $.ajax({
        
        type: 'GET',
        url: '/pluscart',
        data: {
            prod_id:id
        }
        ,
        success: function (data) {
            console.log(data)
            eml.innerText=data.quantity
            price.innerText=data.tamount
            minu.innerText=data.amount
            ajit.innerText=data.totalcost
          
            
           
        }
    })
})
$(".minus-cart").click( function(){
    var id=$(this).attr('pid').toString();
    var eml=this.parentNode.children[2]
    var price=document.getElementById('taamount')
    var minu=document.getElementById('minnu')
    var ajit=document.getElementById('ajit')
    console.log(minu)
    console.log(id)
    $.ajax({
        type:'GET',
        url:'/minus-cart',
        data:{
            prod_id:id
        }
        ,
        success:function(data){
            console.log(data)
            eml.innerText=data.quantity
            price.innerText=data.tamount
            minu.innerText=data.amount
            ajit.innerText=data.totalcost
           
        }
    })
})
$(".removecart").click( function(){
    var id=$(this).attr('pid').toString();
    var price=document.getElementById('taamount')
    var eml=this
    console.log(id)
    $.ajax({
        type:'GET',
        url:'/remove-cart',
        data:{
            prod_id:id
        }
        ,
        success:function(data){
            console.log(data)
            price.innerText=data.tamount
            eml.parentNode.parentNode.parentNode.parentNode.remove()
            
        }
    })
})