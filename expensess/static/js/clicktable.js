
jQuery(function($) {
	console.log("入ったよ")
	//data-hrefの属性をもつtrを選択しclassにclicktableを付加
	$("tr[data-href]").addClass("clickable")

		//くりっくイベント
		.click(function(e) {

			//e.targetはクリックした要素自体、それがa要素意外であれば
			if(!$(e.target).is("a")){

				//その様をの先祖要素で一番近いtrの
				//data-href属性の値に書かれているURLに遷移
				window.location = $(e.target).closest("tr").data("href");}
	});
});