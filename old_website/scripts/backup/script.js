$(document).ready(function(){
	
	alert("first");
	//Constructor for Cell(width,height, cssName (used to move the block), id number)
	var ed_cell = new Cell(1,1,".cell_1",1); //education
	var hs_name_container_cell = new Cell(2,1, '.cell_2', 2);
	var hs_cell = new Cell(1,1,'.cell_3', 3); //headshot
	var name_cell = new Cell(1,1,'.cell_4',4);
	var wdwe_cell = new Cell(1,2,'.cell_5',5); //web dev work exp
	var owe_cell = new Cell(1,1,'.cell_6',6); //other work experience
	var ce_cell = new Cell(1,1,'.cell_7',7); //current enrollment
	var wds_cell = new Cell(1,1,'.cell_8',8); //web dev skills
	var ps_cell = new Cell(1,1,'.cell_9',9); //personal skills
	var hob_cell = new Cell(1,1,'.cell_10',10); //hobbies
	var blank_cell = new Cell(2,1,'.cell_11',11); //blank cell

	//NOTE: id - 1 = index; cells[0] holds ed_cell which has id of 1.
	alert("second");
	var cells = {
		"1" : ed_cell,
		"2" : hs_name_container_cell,
		"3" : hs_cell,
		"4" : name_cell,
		"5" : wdwe_cell,
		"6" : owe_cell,
		"7" : ce_cell,
		"8" : wds_cell,
		"9" : ps_cell,
		"10" : hob_cell,
		"11" : blank_cell	
	};

	var layout1hiddenCells = {
		"2" : false,
		"11" : true
	};

	//"id" : [column, row]
	var layout1positions = {
		"1" : [1,1],
		"2" : [2,1],
		"3" : [2,1],
		"4" : [3,1],
		"5" : [4,1],
		"6" : [5,1],
		"7" : [1,2],
		"8" : [2,2],
		"9" : [3,2],
		"10" : [5,2],
		"11" : [1,3]
	};

	var layout2hiddenCells = {
		"2" : false,
		"11" : false
	};

	//"id" : [column, row]
	var layout2positions = {
		"1" : [1,1],
		"2" : [2,1],
		"3" : [2,1],
		"4" : [3,1],
		"5" : [4,1],
		"6" : [4,3],
		"7" : [1,2],
		"8" : [2,2],
		"9" : [3,2],
		"10" : [3,3],
		"11" : [1,3]
	};

	var layout3hiddenCells = {
		"2" : false,
		"11" : false
	};

	//"id" : [column, row]
	var layout3positions = {
		"1" : [2,2],
		"2" : [1,1],
		"3" : [1,1],
		"4" : [2,1],
		"5" : [3,1],
		"6" : [3,3],
		"7" : [2,3],
		"8" : [1,2],
		"9" : [1,3],
		"10" : [1,4],
		"11" : [2,4]
	};

	var layout4hiddenCells = {
		"2" : false,
		"11" : true
	};

	//"id" : [column, row]
	var layout4positions = {
		"1" : [1,3],
		"2" : [1,1],
		"3" : [1,1],
		"4" : [2,1],
		"5" : [2,2],
		"6" : [1,5],
		"7" : [1,4],
		"8" : [1,2],
		"9" : [2,4],
		"10" : [2,5],
		"11" : [2,4]
	};

	var layout5hiddenCells = {
		"2" : true,
		"11" : true
	};

	//"id" : [column, row]
	var layout5positions = {
		"1" : [1,6],
		"2" : [0,1],
		"3" : [1,2],
		"4" : [1,1],
		"5" : [1,3],
		"6" : [1,9],
		"7" : [1,8],
		"8" : [1,5],
		"9" : [1,7],
		"10" : [1,10],
		"11" : [2,4]
	};

	var PENISMUNCHER = "WHAT THE FUCK";

	//Constructor for Layout: (layoutName, positions, cells, hiddenCells, units)
	var layout1 = new Layout("layout1", layout1positions, cells, layout1hiddenCells, "em");

	//parameters for initializeCellPositions: (cellWidth, cellHeight, margin)
	layout1.initializeCellPositions(5,5,1);

});


function Cell(width, height, cssName, id)
{
	this.width = width; //int
	this.height = height; //int
	this.cssName = cssName; //String
	this.id = id; //String
	this.currentlyHidden = false;
}

//newLeftPosition and newRightPosition must contain units (i.e., 20em, 20px, etc)
Cell.prototype.animateCell = function(newLeftPosition, newTopPosition, timing){
	$(this.cssName).stop().animate({'left': newLeftPosition, 'top': newTopPosition}, timing);
}

Cell.prototype.setPosition = function(leftPosition, topPosition){
	$(this.cssName).css({'left':leftPosition, 'top': topPosition});
}

Cell.prototype.hideCell = function() {
	$(this.cssName).css({'display': 'none'});
}

Cell.prototype.showCell = function() {
	$(this.cssName).css({'display': ''});
}

Cell.prototype.getWidth = function(){
	return this.width;
}

Cell.prototype.getHeight = function(){
	return this.height;
}

Cell.prototype.getId = function(){
	return this.id;
}

//positions is holds the positions of the cells, indexed by id.
//cells holds an array of the cell objects
function Layout(layoutName, positions, cells, hiddenCells, units)
{
	this.layoutName = layoutName;
	this.positions = positions;
	this.cells = cells;
	this.hiddenCells = hiddenCells;
	this.units = units;
}

Layout.prototype.initializeHiddenState = function()
{
	this.cells["2"].currentlyHidden = this.hiddenCells["2"];
	this.cells["11"].currentlyHidden = this.hiddenCells["11"];
}

Layout.prototype.initializeCellPositions = function(cellWidth, cellHeight, margin)
{
	this.initializeHiddenState();
	
	for (var count = 0; count < this.cells.length; count++)
	{
		var currentId = count + 1;
		var currentCell = this.cells[currentId];
		
		//normally we will animate things in a special way if they're hidden
		//since we are initializing, we want to make sure that we hide the blocks we don't want to see
		if (currentCell.currentlyHidden == true)
			currentCell.hideCell();
		else
			currentCell.showCell();
			
		var leftPosition = (this.positions[currentId][0] - 1) * (cellWidth + margin);
		var topPosition = (this.positions[currentId][1] - 1) * (cellHeight + margin);
		
		leftPosition += units;
		topPosition += units;
		
		currentCell.setPosition(leftPosition, topPosition);
	}
}

Layout.prototype.animateCells = function(cellWidth, cellHeight, margin, timing)
{
	//iterates through all of the array cells
	for (var count = 0; count < this.cells.length; count++)
	{
		//the index starts at 0, whereas the id's start at 1
		var currentId = count + 1;
		
		//cells holds a dictionary which uses the id to point to an array.
		//this array holds the position: [column, row].
		//index 0 of this array will give us the column (left position depends on col)
		//index 1 of this array will give us the row (top position depends on row)
		var newLeftPosition = (this.positions[currentId][0] - 1) * (cellWidth + margin);
		var newTopPosition = (this.positions[currentId][1] - 1) * (cellHeight + margin);
		
		newLeftPosition += units;
		newTopPosition += units;
		
		//the final argument this.hidden[currentId] is passed to the Cell.
		//Most of the Cell objects will ignore this, because they only have 3 parameters.
		//For the special Cells, they have special functions for animation.
		this.cells[currentId].animateCell(newLeftPosition, newTopPosition, timing, this.hiddenCells[currentId]);
	}
}


























