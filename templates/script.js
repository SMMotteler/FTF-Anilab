
function addMoreI(){
    ('#ingredients').append("<li>&nbsp;</li>");
    ('#ingredients').append("<li><input type='text' name='ingredients[]' value='' /></li>");
}

function addMoreR(){
    ('#steps').append("<li>&nbsp;</li>");
    ('#steps').append("<li><input type='text' name='recipe_steps[]'  value='' /></li>");
}
