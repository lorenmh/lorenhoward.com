$(document).ready(function(){timing=500;cellInfoHolder=".cell";fontSizeHolder="html";emToPixel=parseInt($(fontSizeHolder).css("font-size"));cellWidthPixels=parseInt($(cellInfoHolder).css("width"));cellHeightPixels=parseInt($(cellInfoHolder).css("height"));cellWidth=20;cellHeight=15;margin=1;units="em";$(".container").removeClass("js-disabled");layout1=new Layout("layout1",layout1positions,cells,layout1hiddenCells,layout1shrunkCells,cellWidth,cellHeight,5,4,margin,units);layout2=new Layout("layout2",layout2positions,cells,layout2hiddenCells,layout2shrunkCells,cellWidth,cellHeight,4,5,margin,units);layout3=new Layout("layout3",layout3positions,cells,layout3hiddenCells,layout3shrunkCells,cellWidth,cellHeight,3,7,margin,units);layout4=new Layout("layout4",layout4positions,cells,layout4hiddenCells,layout4shrunkCells,cellWidth,cellHeight,2,10,margin,units);layout5=new Layout("layout5",layout5positions,cells,layout5hiddenCells,layout5shrunkCells,cellWidth,cellHeight,1,13,margin,units);screenWidth=$(window).width();screenInEm=screenWidth/emToPixel;currentLayout=determineLayout([layout1,layout2,layout3,layout4,layout5],screenInEm);currentLayout.initializeCellPositions();normalCellWidth=layout1.cellWidth;var a=(function(){var b=0;return function(d,c){clearTimeout(b);b=setTimeout(d,c)}})();$(window).resize(function(){a(function(){screenWidth=$(window).width();screenInEm=screenWidth/emToPixel;oldLayout=currentLayout;currentLayout=determineLayout([layout1,layout2,layout3,layout4,layout5],screenInEm);setHtmlDimensions(currentLayout,units);currentLayout.animateCells(oldLayout,timing)},200)})});function setHtmlDimensions(b,a){$("html").css({width:"100%",height:b.layoutHeightAndMargin()+a})}function determineLayout(b,a){if(a>=b[0].layoutWidthAndMargin()){return b[0]}else{if(a>=b[1].layoutWidthAndMargin()){return b[1]}else{if(a>=b[2].layoutWidthAndMargin()){return b[2]}else{if(a>=b[3].layoutWidthAndMargin()){return b[3]}else{return b[4]}}}}}function Cell(b,a,d,c){this.width=b;this.height=a;this.cssName=d;this.cssNameInner="-shrink";this.id=c;this.currentlyHidden=false;this.isCellThatHides=false;this.currentlyShrunk=false;this.isCellThatShrinks=false}Cell.prototype.realWidth=function(c,b,a){return(((this.width*(c+b))-b)+a)};Cell.prototype.realHeight=function(b,c,a){return(((this.height*(b+c))-c)+a)};Cell.prototype.animateCell=function(g,c,f,b,e,a,d){$(this.cssName).stop().animate({left:g,top:c},{duration:d});if(this.isCellThatHides==true){this.hideOrShow(f,e,a,d)}if(this.isCellThatShrinks==true){this.shrinkOrGrow(f,b,e,a,d)}};Cell.prototype.shrinkOrGrow=function(e,b,d,a,c){if(this.currentlyShrunk==true){this.shrinkCell(e,b,a,c)}else{this.growCell(this.realWidth(e,d,a),this.realHeight(b,d,a),c)}};Cell.prototype.hideOrShow=function(d,c,a,b){if(this.currentlyHidden==true){this.hideCell(b)}else{this.showCell(this.realWidth(d,c,a),b)}};Cell.prototype.setPosition=function(b,a){$(this.cssName).css({left:b,top:a})};Cell.prototype.shrinkCell=function(d,b,a,c){var e=this;$(this.cssName+this.cssNameInner).stop().animate({width:d+a,height:b+a},c,function(){$(e.cssName).css({width:d+a,height:b+a})})};Cell.prototype.growCell=function(b,a,c){$(this.cssName).css({width:b,height:a});$(this.cssName+this.cssNameInner).stop().animate({width:b,height:a},c)};Cell.prototype.hideCell=function(a){currentCell=this;$(this.cssName+this.cssNameInner).stop().animate({width:0},a,function(){$(currentCell.cssName).css({display:"none"})})};Cell.prototype.showCell=function(a,b){$(this.cssName).css({display:""});$(this.cssName+this.cssNameInner).stop().animate({width:a},b)};Cell.prototype.getWidth=function(){return this.width};Cell.prototype.getHeight=function(){return this.height};Cell.prototype.getId=function(){return this.id};Cell.prototype.setHiddenState=function(a){this.currentlyHidden=a};Cell.prototype.setShrunkState=function(a){this.currentlyShrunk=a};function Layout(a,e,k,f,c,b,h,j,i,d,g){this.layoutName=a;this.positions=e;this.cells=k;this.hiddenCells=f;this.shrunkCells=c;this.cellWidth=b;this.cellHeight=h;this.layoutWidth=j;this.layoutHeight=i;this.margin=d;this.units=g;this.wrapper=".wrapper";this.container=".container"}Layout.prototype.layoutWidthAndMargin=function(){return((this.layoutWidth*(this.cellWidth+this.margin))-this.margin)};Layout.prototype.layoutHeightAndMargin=function(){return((this.layoutHeight*(this.cellHeight+this.margin))-this.margin)};Layout.prototype.setHiddenState=function(){this.cells["2"].setHiddenState(this.hiddenCells["2"]);this.cells["14"].setHiddenState(this.hiddenCells["14"])};Layout.prototype.setShrunkState=function(){this.cells["1"].setShrunkState(this.shrunkCells["1"]);this.cells["7"].setShrunkState(this.shrunkCells["7"]);this.cells["4"].setShrunkState(this.shrunkCells["4"]);this.cells["9"].setShrunkState(this.shrunkCells["9"])};Layout.prototype.initializeHiddenState=function(){this.cells["2"].setHiddenState(this.hiddenCells["2"]);this.cells["14"].setHiddenState(this.hiddenCells["14"])};Layout.prototype.leftPosition=function(a){return((this.positions[a][0]-1)*(this.cellWidth+this.margin)+this.units)};Layout.prototype.topPosition=function(a){return((this.positions[a][1]-1)*(this.cellHeight+this.margin)+this.units)};Layout.prototype.initializeCellPositions=function(){setHtmlDimensions(this,this.units);this.initializeHiddenState();this.setShrunkState();this.setContainerWidth();for(var a=0;a<Object.keys(this.cells).length;a++){currentId=a+1;currentCell=this.cells[currentId];if(currentCell.isCellThatHides){if(currentCell.currentlyHidden){currentCell.hideCell(0)}else{currentCell.showCell()}}if(currentCell.isCellThatShrinks){if(currentCell.currentlyShrunk){currentCell.shrinkCell(this.cellWidth,this.cellHeight,this.units,0)}else{currentCell.growCell(currentCell.realWidth(this.cellWidth,this.margin,this.units),currentCell.realHeight(this.cellHeight,this.margin,this.units),0)}}currentCell.setPosition(this.leftPosition(currentId),this.topPosition(currentId))}};Layout.prototype.animateLeftMargin=function(a,b){this.setLeftMargin(this.getLeftMarginValue(a));$(".wrapper").stop().animate({marginLeft:0},b)};Layout.prototype.getLeftMarginValue=function(a){return((this.layoutWidthAndMargin()-a.layoutWidthAndMargin())/2)};Layout.prototype.setLeftMargin=function(a){$(this.wrapper).css({"margin-left":a+this.units})};Layout.prototype.setContainerWidth=function(){$(this.container).css({width:this.layoutWidthAndMargin()+this.units})};Layout.prototype.animateCells=function(b,d){this.setHiddenState();this.setShrunkState();this.setContainerWidth();this.animateLeftMargin(b,d);for(var c=0;c<Object.keys(this.cells).length;c++){var a=c+1;this.cells[a].animateCell(this.leftPosition(a),this.topPosition(a),this.cellWidth,this.cellHeight,this.margin,this.units,d)}};first=new Cell(2,2,".cell_1",1);third_fourth_container_cell=new Cell(2,1,".cell_2",2);third=new Cell(1,1,".cell_3",3);fourth=new Cell(1,2,".cell_4",4);fifth=new Cell(1,1,".cell_5",5);sixth=new Cell(1,1,".cell_6",6);seventh=new Cell(2,2,".cell_7",7);eighth=new Cell(1,2,".cell_8",8);ninth=new Cell(2,1,".cell_9",9);tenth=new Cell(1,1,".cell_10",10);eleventh=new Cell(1,1,".cell_11",11);twelfth=new Cell(1,1,".cell_12",12);thirteenth=new Cell(1,1,".cell_13",13);blank_cell=new Cell(2,1,".cell_14",14);first.isCellThatShrinks=true;seventh.isCellThatShrinks=true;fourth.isCellThatShrinks=true;ninth.isCellThatShrinks=true;third_fourth_container_cell.isCellThatHides=true;blank_cell.isCellThatHides=true;cells={"1":first,"2":third_fourth_container_cell,"3":third,"4":fourth,"5":fifth,"6":sixth,"7":seventh,"8":eighth,"9":ninth,"10":tenth,"11":eleventh,"12":twelfth,"13":thirteenth,"14":blank_cell};layout1hiddenCells={"2":false,"14":true};layout1shrunkCells={"1":false,"7":false,"4":true,"9":false};layout1positions={"1":[4,1],"2":[2,1],"3":[2,1],"4":[3,1],"5":[3,2],"6":[1,1],"7":[1,2],"8":[5,3],"9":[3,3],"10":[1,4],"11":[2,4],"12":[3,4],"13":[4,4],"14":[4,4]};layout2hiddenCells={"2":false,"14":true};layout2shrunkCells={"1":false,"7":false,"4":true,"9":false};layout2positions={"1":[3,1],"2":[1,1],"3":[1,1],"4":[2,1],"5":[3,3],"6":[4,3],"7":[1,2],"8":[4,4],"9":[2,4],"10":[1,4],"11":[1,5],"12":[2,5],"13":[3,5],"14":[3,5]};layout3hiddenCells={"2":false,"14":false};layout3shrunkCells={"1":false,"7":false,"4":true,"9":false};layout3positions={"1":[2,2],"2":[1,1],"3":[1,1],"4":[2,1],"5":[3,1],"6":[1,2],"7":[1,4],"8":[3,4],"9":[2,6],"10":[1,3],"11":[1,6],"12":[1,7],"13":[2,7],"14":[2,7]};layout4hiddenCells={"2":false,"14":true};layout4shrunkCells={"1":false,"7":false,"4":true,"9":false};layout4positions={"1":[1,2],"2":[1,1],"3":[1,1],"4":[2,1],"5":[1,4],"6":[2,4],"7":[1,5],"8":[2,8],"9":[1,7],"10":[1,8],"11":[1,9],"12":[1,10],"13":[2,10],"14":[2,10]};layout5hiddenCells={"2":true,"14":true};layout5shrunkCells={"1":true,"7":true,"4":false,"9":true};layout5positions={"1":[1,3],"2":[0,1],"3":[1,1],"4":[1,1],"5":[1,4],"6":[1,5],"7":[1,6],"8":[1,9],"9":[1,7],"10":[1,8],"11":[1,11],"12":[1,12],"13":[1,13],"14":[1,13]};