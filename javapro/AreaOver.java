class Area
{

final static float pi = 3.14f;

void findArea(float r)
{
float ca= pi*r*r;
System.out.println("Area of circle:"+ca);
}

void findArea(int l, int b)
{
int ra= l*b;
System.out.println("Area of Rectangle:"+ra);
}

void findArea(int s)
{
int sa = s*s;
int sp = 4*s;
System.out.println("Area of square:"+sa);
System.out.println("Perimeter of square:"+sp);
}
}

class AreaOver
{
	public static void main(String[] args) 
	{
		Area fa = new Area();
		fa.findArea(5);
		fa.findArea(10,20);
		fa.findArea(10.0f);
	}
}