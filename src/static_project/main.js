$(document).ready(function(){
    console.log('hello world')
    $('#modal-btn').click(function(){
        console.log('working')
        $('.ui.modal')
        .modal('show')
        ;
    })
    $('.ui.dropdown').dropdown()
    

})

$('.SeeMore2').click(function(){
    var $this = $(this);
    $this.toggleClass('SeeMore2');
    if($this.hasClass('SeeMore2')){
        $this.text('daha fazla göster');         
    } else {
        $this.text('daha az göster');
    }
});

$('.special.cards .image').dimmer({
    on: 'hover'
  });


