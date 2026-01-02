frappe.ready(function () {
	// هنسيب الكود يشتغل في أي صفحة، ولو الـ div مش موجود مش هيعمل حاجة
	const grid = document.getElementById('courses-grid');
	const empty = document.getElementById('courses-empty');

	// لو مفيش grid خلاص نخرج
	if (!grid) return;

	frappe.call({
		method: 'lms.lms.utils.get_courses',
		args: {
			doctype: 'LMS Course',
			filters: { published: 1 },
			start: 0,
			limit: 30,
		},
		callback: function (r) {
			console.log('get_courses response:', r.message);

			let data = r.message || [];
			const courses = Array.isArray(data.courses) ? data.courses : data;

			if (!courses || !courses.length) {
				if (empty) empty.style.display = 'block';
				return;
			}

			courses.forEach(function (course) {
				const img = course.course_image || '';
				const name = course.course_name || course.name || 'Course';
				const intro = course.short_introduction || '';
				const price = course.course_price || 0;

				const card = document.createElement('div');
				card.className = 'course-card';
				card.innerHTML = `
                    <img src="${img}" class="course-img">
                    <div class="course-body">
                        <div class="course-name">${name}</div>
                        <div class="course-desc">${intro}</div>
                    </div>
                    <div class="course-footer">
                        <div class="course-price">${price} ر.س</div>
                        <a class="course-btn" href="/lms/courses/${course.name}">
                            View Course
                        </a>
                    </div>
                `;
				grid.appendChild(card);
			});
		},
		error: function (err) {
			console.error('Error loading courses', err);
			if (empty) {
				empty.style.display = 'block';
				empty.innerText = 'حدث خطأ أثناء تحميل الكورسات.';
			}
		},
	});
});
