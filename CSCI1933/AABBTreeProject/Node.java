import java.awt.*;
import java.util.*;

//riehl046

public class Node {

	private Node left; // null if leaf
	private Node right; // null if leaf
	private Shape shape; // non-null if leaf
	private Bounds bounds; // always set in constructor

	// Getters and setters
	// Use for unit tests!
	public Node getLeft(){ return left; }
	public Node getRight(){ return right; }
	public Shape getShape(){ return shape; }
	public Bounds getBounds(){ return bounds; }
	public void setLeft( Node l ){ left = l; }
	public void setRight( Node r ){ right = r; }
	public void setShape( Shape s ){ shape = s; }
	public void setBounds( Bounds b ){ bounds = b; }

	// TODO
	// 2) The constructor takes a stack of shapes and an (initial) splitting plane axis.
	// If there is one shape, then it stores the reference and becomes a leaf node.
	// If there are two or more shapes, it will partition the stack into seperate stacks,
	// create children, and pass the stacks to the children.
	// This is what we call top-down tree construction.
	public Node(Stack<Shape> stack, int axis){

		// Set our objects to null, so we know not to use
		// them if they are never set.
		left = null;
		right = null;
		shape = null;
		bounds = new Bounds();

		// We should never have an empty stack!
		if( stack.size() == 0 ){
		        throw new RuntimeException("**Node Error: Empty stack!");
		}
		// 2a) If our stack only has one shape, we are a leaf node!
		if(stack.size() == 1){
		    bounds = stack.peek().getBounds();
			shape = stack.pop();
			return;
		}

		// 2b) Extend our bounding box to contain everything in the stack
		for(int i = 0; i < stack.size();i++){
			bounds.extend(stack.elementAt(i).getBounds());
		}
		Stack<Shape> leftS = new Stack();
		Stack<Shape> rightS = new Stack();
		// 3) Now, split the stack!
		splitStack(stack,axis,leftS,rightS);

		// Do a recursive construction by making new Node (children).
		//
		// Here, we switch the axis between 1 and 2, which is called a
		// "round robin splitting plane". So if our current node was split on the
		// x axis, the children will be split along the y axis. There are significantly
		// better ways to determining where (and how) to split, and these are the
		// kinds of problems we deal with in Computer Graphics research.
        int newAxis;
        if(axis == 1) newAxis = 0;
        else newAxis = 1;
        this.left = new Node(leftS,newAxis);
        this.right = new Node(rightS,newAxis);


	} // end constructor


	// 3) To decide which shape goes on which stack, we'll compute
	// the center of all objects currently in the stack. Objects that are less than the median
	// go on the left stack, greater than or equal to on the right.
	public void splitStack(Stack<Shape> stack, int axis, Stack<Shape> leftStack, Stack<Shape> rightStack){

		// We should never call split stack with an empty stack.
		if( stack.size() == 0 ){
		        throw new RuntimeException("**Node Error: Empty stack!");
		}

		// 3a) First, compute the centroid. This is the average of all vertices.
		// We'll use an iterator so we don't change the stack (yet).
        double sum;
		if(axis == 0) sum = getXSum(stack);
		else sum = getYSum(stack);
		double average = sum / ((double) stack.size());

		// 3b) Now that we know the center, we can partition the stack
		// into two seperate ones!
		if(axis == 0){
		    while(stack.size() != 0){
		        Shape a = stack.pop();
		        if(a.getCenter().x > average) rightStack.add(a);
		        else leftStack.add(a);
            }
        }
        else{
		    while(stack.size() != 0){
		        Shape a = stack.pop();
		        if(a.getCenter().y > average) rightStack.add(a);
		        else leftStack.add(a);
            }
        }
		if(leftStack.size() == 0 || rightStack.size() == 0) throw new RuntimeException("*Sees your raised exception* oWo whats this?\n" + leftStack.size() + "\n" + rightStack.size());

		// Make sure both stacks have at least one element.
		// There are two ways this error would trigger:
		// -You made a mistake in your stack splitting
		// -Two elements have the same center along a specific axis (possible, but unlikely).
		if( leftStack.empty() || rightStack.empty() ){
			throw new RuntimeException("**splitStack Error: Empty child stack after split!");
		}

	} // end split stack

    private double getXSum(Stack<Shape> a){
	    double sum = 0;
	    for(int i = 0; i < a.size(); i++){
	        sum += a.elementAt(i).getCenter().x;
        }
        return sum;
    }

    private double getYSum(Stack<Shape> a){
        double sum = 0;
        for(int i = 0; i < a.size(); i++){
            sum += a.elementAt(i).getCenter().y;
        }
        return sum;
    }

	// TODO
	// 4) Traverse the tree and find the selected shape.
	// If we're a leaf, test against the shape.
	// If we're a node, test children.
	// Only one shape should be selected at a time.
	public boolean select(double x, double y, int[] counter){
		counter[0]++; // Don't remove this

		// 4a) If we're outside the bounds of the node, we
		// don't need to check children!
		if(bounds.isOutside(x,y)) return false;
		// 4b) If we are a leaf, check the shape
		if(left == null && right == null) return shape.select(x,y);

		// If we aren't a leaf, we should have both
		// a left and right child.

		// 4c) Otherwise, traverse children!
		return (left.select(x,y,counter) || right.select(x,y,counter));


		// Since we assume no overlapping shapes, return true
		// if one was found.



	} // end select

	// Returns true if it finds a closer shape, in which is sets shapeRef and currentMin.
	// currentMin is ONLY updated when a closer shape is found.
	public boolean nearest(double x, double y, double[] currentMin, Shape[] shapeRef, int[] counter){
		counter[0]++; // Don't remove this

		// 5a) Check exterior distance between point and AABB.
		// If it's larger than the current min, return false
		// (since we know we're farther away than the current min).

		// 5b) If we are a leaf, check exterior distance
		// between the point and shape. If that exterior distance
		// is less than the current min, update the shapeRef
		// and currentMin, then return true.

		// If we aren't a leaf, we should have both
		// a left and right child.
		if( right == null || left == null ){
			throw new NullPointerException();
		}

		// 5c) Otherwise, traverse children!
		// As in select, we'll try to minimize tree traversal.
		// See which node is closer and traverse that branch first.

		return false;

	} // end nearest

	// Draw the boundaries of the node and children
	public void paint(Graphics2D g){

		// Our bounds should visibly enclose everything below it on the tree.
		bounds.paint(g);

		// If we're a leaf node, draw the shape contained by this node:
		if( shape != null ){
			return;
		}

		// If we aren't a leaf, we should have both
		// a left and right child.
		if( right == null || left == null ){
			throw new NullPointerException();
		}

		left.paint(g);
		right.paint(g);

	} // end paint


} // end class Node
