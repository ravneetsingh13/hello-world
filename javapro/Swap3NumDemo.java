//This program will swap value of x with y, y with z and z with x i.e. (3,8,4) ---> (8,4,3)
class Swap3Num
{
	void swapNum(int x,int y,int z)
	{
		System.out.println("Original values= "+x+" "+y+" "+z);
		x=x+y+z; //x=15, y=8, z=4
		z=x-y-z; //x=15, y=8, z=3
		y=x-y-z; //x=15, y=4 ,z=3
		x=x-y-z; //x=8, y=4, z=3
		System.out.println("After Swapping= "+x+" "+y+" "+z);
	}
}

class Swap3NumDemo 
{
	public static void main(String[] args) 
	{
		Swap3Num sn=new Swap3Num();
		sn.swapNum(3,8,4);
		sn.swapNum(10,20,30);
		sn.swapNum(-53,-81,-99);
		sn.swapNum(9,1,0);
	}
}
