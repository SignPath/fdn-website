document.addEventListener("DOMContentLoaded", () => {
  initCarousel();
  filterProjects();
});

function initCarousel() {
	/**
	 * carousel has the following items
	 * 
	 *                       Viewport
	 *            +---------------------------+
	 * .out-left  | .active   .show   .show   | .out-right
	 *            +---------------------------+
	 * 
	 */
	document.querySelectorAll("div.carousel").forEach((carousel) => {

		function getNumCarouselItems() {
			let bodyWidth = document.body.clientWidth;
			if (bodyWidth > 1000) return 3;
			if (bodyWidth > 700) return 2;
			return 1; 
		}

		let numCarouselItems = getNumCarouselItems();

		// initialize carousel
		carousel.querySelectorAll('li').forEach((li, i) => {
			if (i == 0) { li.classList.add('out-left'); } else
			if (i == 1) { li.classList.add('active'); } else 
			if (i == numCarouselItems + 1) { li.classList.add('out-right'); } else
			if (i <= numCarouselItems) { li.classList.add('show'); }
		});

		carousel.querySelectorAll('a').forEach((a, i) => {
			if (i == 0) {
				a.addEventListener('click', function(e) {
					let ul = e.currentTarget.parentNode.querySelector('ul');
					moveCarousel(ul, true);
					startAutoMovement();
					e.preventDefault();
				});
			} else {
				a.addEventListener('click', function(e) {
					let ul = e.currentTarget.parentNode.querySelector('ul');
					moveCarousel(ul, false);
					startAutoMovement();
					e.preventDefault();
				})
			}
		})

		// constantly moving
		let interval = undefined;
		function startAutoMovement() {
			if (interval) {
				clearInterval(interval);
				interval = undefined;
			}
			interval = setInterval(function() {
				moveCarousel(carousel.querySelector('ul'), false);
			}, 3000)
		}

		startAutoMovement();

		function moveCarousel(ul, moveRight) {
			function normalizeIndex(index) {
				function inner() {
					if (index < 0) return ul.children.length + index;
					if (index >= ul.children.length) return index - ul.children.length;
					return index;
				}
				let r = inner();
				return r;
			}

			let activeElem = ul.querySelector('li.active');
			let currentIndex = Array.from(ul.children).indexOf(activeElem);
			let leftItem = ul.children[normalizeIndex(currentIndex-1)];
			let showItems = Array.from({length: numCarouselItems - 1}, (_, i) => ul.children[normalizeIndex(currentIndex + 1 + i)]);
			let rightItem = ul.children[normalizeIndex(currentIndex + numCarouselItems)];
			console.log(showItems);

			leftItem.classList.remove('out-left');
			if (moveRight) leftItem.classList.add('active');
			leftItem.style.order = moveRight ? 1 : 'initial';

			activeElem.classList.remove('active');
			activeElem.classList.add(moveRight ? 'show' : 'out-left');
			activeElem.style.order = moveRight ? 2 : 0;

			showItems.forEach((showItem, i) => {
				if (i == 0 && !moveRight) {
					showItem.classList.remove('show');
					showItem.classList.add('active');
				}
				if ((i == numCarouselItems - 2) && moveRight) {
					showItem.classList.remove('show');
					showItem.classList.add('out-right');
				}
				showItem.style.order = moveRight ? (3 + i) : (1 + i);
			});
			rightItem.classList.remove('out-right');
			if (!moveRight) rightItem.classList.add(numCarouselItems == 1 ? 'active' : 'show');
			rightItem.style.order = moveRight ? 'initial' : numCarouselItems;

			// add new left out / right-out items
			if (moveRight) {
				ul.children[normalizeIndex(currentIndex - 2)].classList.add('out-left');
				ul.children[normalizeIndex(currentIndex - 2)].style.order = 0;
			} else {
				ul.children[normalizeIndex(currentIndex + numCarouselItems + 1)].classList.add('out-right');
				ul.children[normalizeIndex(currentIndex + numCarouselItems + 1)].style.order = (numCarouselItems + 1);
			}
		}

		
	})
}

function filterProjects() {
	// parse url to already show hide components on startup
	const url = new URL(location);
	let searchTerm = url.searchParams.get('search') || '';
	let category = url.searchParams.get('category') || 'all';
	filter_projects_internal(category, searchTerm);

	var search_field = document.getElementById('projects-search-field');
	var category_select = document.getElementById('projects-category-select');
	if (search_field && category_select) {
		search_field.value = searchTerm;
		category_select.value = category;

		search_field.addEventListener('input', function(e) {
			// change url
			const url = new URL(location);
			if (e.target.value == '') {
				url.searchParams.delete('search');
				history.replaceState({}, "", url);
			} else {
				url.searchParams.set('search', e.target.value);
				history.pushState({}, '', url);
			}

			filter_projects_internal(category_select.value, e.target.value);
		});

		category_select.addEventListener('change', function(e) {
			const url = new URL(location);
			if (category_select.value == 'all') {
				url.searchParams.delete("category")
			} else {
				url.searchParams.set("category", category_select.value);
			}
			history.pushState({}, "", url);
			

			filter_projects_internal(category_select.value, search_field.value);
		});
	}
}

function filter_projects_internal(category, searchTerm) {
	document.querySelectorAll('ul.projects li').forEach(function(listItem) {
		let categoryMatches = (category == 'all') || listItem.dataset.category == category;
		let searchTermMatches = (searchTerm.length == 0) || listItem.title.toLowerCase().includes(searchTerm.toLowerCase());
		listItem.style.display = (categoryMatches && searchTermMatches) ? 'block' : 'none';
	});
}
