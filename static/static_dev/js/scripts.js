$(document).ready(function () {
    var form = $('#form_buying_product');
    var amount = 0;
    form.on('submit', function (e) {
        e.preventDefault();
        amount += 1;
        var submit_btn = $("#submit_btn");
        var product_id = submit_btn.data("product_id");
        var product_name = submit_btn.data("name");
        var product_price = submit_btn.data("price");

        var data = {};
        data.product_id = product_id;
        data.amount = amount;
        var csrf_token = $('#form_buying_product [name = "csrfmiddlewaretoken"]').val();
        data["csrfmiddlewaretoken"] = csrf_token;

        var url = form.attr("action");
        $.ajax({
            url: url,
            type: 'POST',
            data: data,
            cache: true,
            success: function (data) {
                console.log("OK");
                if (data.products_total_amount) {
                    $('#basket_total_amount').text(data.products_total_amount);
                }
            },
            error: function () {
                console.log("error");
            }
        });


        $('.basket-container ul').append('<li>' + product_name + '  ' + amount + 'шт.  ' + product_price*amount + '₽' +
            ' ' + '<a class="delete-item" href="">x</a>' + '</li>');
    });

    function showingBasket(){
        $('.basket-items').toggleClass('hidden');
    }

    $('.basket-container').on('click', function(e){
       e.preventDefault();
       showingBasket();
    });

     $('.basket-container').mouseover(function(){
         showingBasket();
     });

     $('.basket-container').mouseout(function(){
        showingBasket();
     });

     $(document).on('click', '.delete-item', function (e) {
         e.preventDefault();
         $(this).closest('li').remove();
     })
});