class SwapNum
{
	void swap(int x, int y)
	{
		x=x+y;
		y=x-y;
		x=x-y;
		System.out.println(x+" "+y);
	}
}

class Swap 
{
	public static void main(String[] args) 
	{
		SwapNum s = new SwapNum();
		s.swap(1,0);
		s.swap(-10,-20);
		s.swap(999,99);
	}
}
