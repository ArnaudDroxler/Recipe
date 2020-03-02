

var ingredient_max = 25;
var ingredient_count = 1;

var ingredient_template = $("#ingredient_template").html();
var ingredient_target = $("#ingredient_target")
var ingredient_inputRow = [];


var instruction_max = 25;
var instruction_count = 1;

var instruction_template = $("#instruction_template").html();
var instruction_target = $("#instruction_target")
var instruction_inputRow = [];

$( "#add_ingredient" ).click(function() {
    add_ingredient_rows()
});

$( "#remove_ingredient" ).click(function() {
    remove_ingredient_rows()
});

function add_ingredient_rows(){
    if(ingredient_count <= ingredient_max){
      inputRow = {
        count : ingredient_count
      }
      var html = Mustache.render(ingredient_template, inputRow);
      ingredient_target.append(html);
      ingredient_count++;
    }
  }
  
function remove_ingredient_rows(){
    ingredient_target.find('#ingredient_row').last().remove();
    if(ingredient_count <= 1){
        ingredient_count = 1;
    }else{
        ingredient_count--;
    }
}


$( "#add_instruction" ).click(function() {
    add_instruction_rows()
});

$( "#remove_instruction" ).click(function() {
    remove_instruction_rows()
});

function add_instruction_rows(){
    if(instruction_count <= instruction_max){
      inputRow = {
        count : instruction_count
      }
      var html = Mustache.render(instruction_template, inputRow);
      instruction_target.append(html);
      instruction_count++;
    }
  }
  
function remove_instruction_rows(){
    instruction_target.find('#instruction_row').last().remove();
    if(instruction_count <= 1){
        instruction_count = 1;
    }else{
        instruction_count--;
    }
}


add_ingredient_rows()
add_instruction_rows()