
$( function() { loadplayer(); });


function music() {

	contentDiv = $('#content');
	contentDiv.show();
}

function loadplayer() {

	contentDiv = $('#content');
	$.ajax({

		url: "/musicplayer",
		context: document.body,
		dataType: "json"

		   }).done( 
		   		function(data) { contentDiv.append(data['embed']); contentDiv.hide(); }
					);

}

function shows() {
	 
	contentDiv = $('#content');
	contentDiv.toggle();
	contentDiv.append('<table style="width:100%"><tr><td>Jill</td><td>Smith</td> <td>50</td></tr><tr><td>Eve</td><td>Jackson</td> <td>94</td></t</table>');
}

function home() {
	
	contentDiv = $('#content');
	contentDiv.hide();
}

