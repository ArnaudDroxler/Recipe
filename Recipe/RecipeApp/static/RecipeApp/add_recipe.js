

var ingredient_max = 25
var ingredient_count = 0

var ingredient_template = $("#ingredient_template").html();
var ingredient_target = $("#ingredient_target")
var ingredient_count_input = $("#ingredient_count")

var instruction_max = 25
var instruction_count = 0

var instruction_template = $("#instruction_template").html();
var instruction_target = $("#instruction_target")
var instruction_count_input = $("#instruction_count")


$( "#add_ingredient" ).click(function() {
    add_ingredient_rows()
});

$( "#remove_ingredient" ).click(function() {
    remove_ingredient_rows()
});

function add_ingredient_rows(){
    if(ingredient_count <= ingredient_max){
        var html = ingredient_template.split('[[ count ]]').join(ingredient_count)
        ingredient_target.append(html)
        ingredient_count++
        ingredient_count_input.val(ingredient_count)
    }
  }
  
function remove_ingredient_rows(){
    ingredient_target.find('#ingredient_row').last().remove();
    if(ingredient_count <= 1){
        ingredient_count = 1
    }else{
        ingredient_count--
    }
    ingredient_count_input.val(ingredient_count)
}


$( "#add_instruction" ).click(function() {
    add_instruction_rows()
});

$( "#remove_instruction" ).click(function() {
    remove_instruction_rows()
});

function add_instruction_rows(){
    if(instruction_count <= instruction_max){
        var html = instruction_template.split('[[ count ]]').join(instruction_count)
        html = html.split('[[ count+1 ]]').join(instruction_count+1)
        instruction_target.append(html)
        instruction_count++
        instruction_count_input.val(instruction_count)
    }
  }
  
function remove_instruction_rows(){
    instruction_target.find('#instruction_row').last().remove();
    if(instruction_count <= 1){
        instruction_count = 1
    }else{
        instruction_count--
    }
    instruction_count_input.val(instruction_count)
}


add_ingredient_rows()
add_instruction_rows()