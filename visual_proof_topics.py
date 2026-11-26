"""Narration and curriculum metadata for the visual proof queue."""

FPS = 30

def proof(topic_id, title, curricula, *narration):
    return dict(id=topic_id, title=title, visual="visual_proof", curricula=curricula,
                segments=[{"narration": line} for line in narration])


PROOFS = [
    proof("diff_of_squares", "Difference of Squares", "HKDSE · IB AA · MPM2D",
          "Start with a square of side a. Slide out a corner square of side b.",
          "Cut off the exposed strip. Give it a quarter turn, then slide it flush against the lower rectangle.",
          "The same area now fills a rectangle. Its height is a minus b, and its width is a plus b."),
    proof("arithmetic_series", "Sum of an Arithmetic Staircase", "HKDSE · IB AA/AI · MCR3U",
          "Arrange one plus two plus three plus four as a staircase. The same construction works with n rows.",
          "Make a second staircase with exactly the same number of tiles.",
          "Turn it half a revolution and fit it into the gaps. The pair fills n rows of n plus one tiles, so take half."),
    proof("triangle_area_sine", "Triangle Area from Two Sides and an Angle", "HKDSE · IB AA/AI · MPM2D",
          "Use side a as the base. Side b makes the included angle C with it.",
          "Drop the perpendicular from the top vertex. Its height is opposite angle C, so it is b times sine C.",
          "A turned copy makes a parallelogram with the same base and height. Half its area is one half a b sine C."),
    proof("unit_circle_identity", "Why Sine Squared Plus Cosine Squared Equals One", "HKDSE · IB AA/AI · MHF4U",
          "Rotate a radius around the unit circle. Its length stays one.",
          "The horizontal leg measures cosine theta. The vertical leg measures sine theta.",
          "As the triangle changes, Pythagoras still holds. The two leg squares always add to the radius squared, which is one."),
    proof("circle_centre_angle", "The Centre Angle Is Twice the Circumference Angle", "HKDSE · IB AA/AI · MPM2D enrichment",
          "Keep A and B fixed. Move P along the major arc and watch its two chords.",
          "Extend the radius through P to the opposite point. It splits the picture into two isosceles triangles. Each exterior angle at the centre is twice its matching base angle at P.",
          "Add the pairs when the diameter lies inside the angle at P. As it moves outside, subtract the smaller angles instead. The two to one relationship still holds."),
    proof("sum_of_odd_numbers", "Odd Numbers Build Squares", "HKDSE · IB AA/AI · MCR3U",
          "Start with one square. Three tiles form an L that grows it into a two by two square.",
          "The next L has five tiles. Slide it into place to make a three by three square.",
          "Seven more tiles make four by four. The nth layer adds two n minus one tiles, so the first n odd numbers fill an n by n square."),
    proof("geometric_series_half", "One Half Plus One Quarter Plus One Eighth", "HKDSE · IB AA/AI · MHF4U",
          "Cut a unit square in half. Keep one piece and leave the other half uncoloured.",
          "Halve the remainder twice more. The next coloured areas are one quarter and one eighth of the original square.",
          "Every cut halves the uncoloured area. It tends to zero, so the infinite sum is exactly the area of the unit square."),
    proof("derivative_x_squared", "The Area Proof of the Derivative of X Squared", "HKDSE M1/M2 · IB AA/AI · MCV4U",
          "Grow a square of side x by a small amount on two adjacent sides.",
          "The added area is two strips, each x times delta x, and a corner of area delta x squared.",
          "Divide the change in area by delta x. As the corner contribution tends to zero, the rate tends to two x."),
    proof("law_of_cosines", "A Geometric Proof of the Cosine Law", "HKDSE · IB AA/AI · MPM2D",
          "Build squares on the three sides of an oblique triangle. The square opposite angle C has area c squared.",
          "Drop a perpendicular to the line through side a. The height is b sine C. The horizontal leg is the length of a minus the signed projection b cosine C. Apply Pythagoras.",
          "Expand the square and combine the sine and cosine squares. Their sum is one, leaving a squared plus b squared minus two a b cosine C."),
    proof("completing_the_square_morph", "Completing the Square by Rearranging Area", "HKDSE · IB AA · MPM2D",
          "Place a rectangle of area b x beside a square of area x squared. Split the rectangle into two equal strips.",
          "Rotate one strip and slide it below the original square. The strips now meet a missing corner.",
          "Fill that corner with a square of side b over two. The completed square has side x plus b over two."),
]
