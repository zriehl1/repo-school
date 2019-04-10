import java.awt.*;

//riehl046

public class Bounds {

	// The extrema of our rectangle
	private Vec2 min;
	private Vec2 max;

	// Getters, no setters. Use extend instead.
	public Vec2 getMin(){ return min; }
	public Vec2 getMax(){ return max; }

	// Default min and max to null, so that they are
	// initialized on the first call to extend.
	public Bounds(){
		min = null;
		max = null;
	}

	// Check if a point is outside the bounds of the box
	// Ignore z axis for this function
	public boolean isOutside(double x, double y){
		if( x > max.x || x < min.x) return true;
		else if( y > max.y || y < min.y) return true;
		return false;
	}

	// Extend the size of the box to include a new point
	public void extend(double x, double y){
		// If we haven't set min or max yet, do so now.
		if(min == null) min = new Vec2();
		if(max == null) max = new Vec2();
		if(x >= max.x) max.x = x;
		else min.x = x;
		if(y >= max.y) max.y = y;
		else min.y = y;

	}


	// Returns the distance from the box surface to a point
	// Return 0 if the point is inside the box!
	public double exteriorDistance(double x, double y){
		if(!(isOutside(x,y))) return 0;
		Vec2 point = new Vec2(x,y);
		double one = max.distance(point);
		double two = min.distance(point);
		return Math.min(one,two);


	}


	// Extend the size of the box to include a new bounds
	public void extend(Bounds b){
		if(min == null) min = new Vec2();
		if(max == null) max = new Vec2();
		if(b.max.x > max.x) max.x = b.max.x;
		if(b.max.y > max.y) max.y = b.max.y;
		if(b.min.x < min.x) min.x = b.min.x;
		if(b.min.y < min.y) min.y = b.min.y;

	}

	// Draw a black opaque rectangle
	public void paint(Graphics2D g){
		g.setColor(Color.black);
		g.drawRect((int)min.x, (int)min.y, (int)(max.x-min.x), (int)(max.y-min.y));
	}

} // end class Bounds
