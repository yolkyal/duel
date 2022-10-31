def is_rect_pt_collision(rect, pt):
	return pt[0] >= rect[0] and pt[1] >= rect[1] and pt[0] <= rect[0] + rect[2] and pt[1] <= rect[1] + rect[3]