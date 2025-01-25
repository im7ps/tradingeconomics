document.querySelectorAll('path').forEach(path => {
    path.addEventListener('click', (event) => {
        event.target.style.fill = 'blue';
		let label = event.target.getAttribute("name");
		if (label == null)
		{
			label = event.target.getAttribute("class");
		}
        if (label == "Mexico") {
			window.location.href = "mexico.html"
		}
		else
		{
			alert("Free users have access only to Mexico.")
		}
    });
});

