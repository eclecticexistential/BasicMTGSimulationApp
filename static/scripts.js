var $submit = $('#submit');
var $counter = $('#counter');
var $format = $('#format');
var $mana = $('#mana');
var $evo = $('#evo');
var $lands = $('#lands');
var $removal = $('#removal');
var $life_gain = $('#life_gain');
var $tutor = $('#tutor');
var $draw_cards = $('#draw_cards');
var $combat_tricks = $('#combat_tricks');
var $lil = $('#lil');
var $bombs = $('#bombs');
var $stats = [];
var $area = $('#area');
var $here = $('#here');
var $reset = $('#configreset');

$(document).ready(function () {

    $('.count').change(function () {
        var count = 0;
        $('.count').each(function () {
            count+= Number($(this).val())
        });
        $counter.html(count);
    })
});

$(document).ready(function () {
    $("#format").change(function () {
        var val = $(this).val();
    });
    $("#lands").change(function () {
        var val = $(this).val();
    });
    $("#removal").change(function () {
        var val = $(this).val();
    });
    $("#life_gain").change(function () {
        var val = $(this).val();
    });
    $("#tutor").change(function () {
        var val = $(this).val();
    });
    $("#draw_cards").change(function () {
        var val = $(this).val();
    });
    $("#combat_tricks").change(function () {
        var val = $(this).val();
    });
    $("#lil").change(function () {
        var val = $(this).val();
    });
    $("#bombs").change(function () {
        var val = $(this).val();
    });
});

$submit.on("click", function(){
    $tots = Number($lands.val()) + Number($lil.val()) + Number($bombs.val())+ Number($removal.val()) + Number($life_gain.val()) + Number($tutor.val()) + Number($draw_cards.val()) + Number($combat_tricks.val())
    if($tots != $format.val()){
        if($lands.val() == ''){
            alert("Need number of lands.")
        }
        if($mana.val() == ''){
            alert("How many sources of mana?")
        }
        if($evo.val() == ''){
            alert("Must include some amount of evos.")
        }
        if($bombs.val() == ''){
            alert("A few big creatures are needed.")
        }
        if($lil.val() == ''){
            alert("Gotta include chump blockers.")
        }
    }
    else{
        if($stats.length == 0){
        data=String([$format.val(), $mana.val(), $lands.val(), $removal.val(), $life_gain.val(), $tutor.val(), $draw_cards.val(), $combat_tricks.val(), $lil.val(), $bombs.val(), $evo.val()])
        $here.val(data)
        }
        else{
            $stats = []
        }
    }
})

$reset.on("click", function(){
    $("select").val("0");
    $('#here').val("");
})