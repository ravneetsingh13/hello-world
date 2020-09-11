class Solution {
    public int findLucky(int[] arr) {
        int temp,m;
        for(int i=0;i<arr.length-1;i++)
        {
            for(int j=i;j>0;j--)
            {
                if(arr[j]>arr[j+1])
                {
                temp=arr[i+1];
                arr[i+1]=arr[i];
                arr[i]=temp;
                }
            }
        }
        for (int i = 0; i < arr.length; i++) {
     System.out.println(arr[i]);
   }
        return 1;
    }
}
class StringDemo
{
	public static void main(String args[])
	{
		int[] arr1 = {3,1,2,2,3,3,4,2,4,2};
		Solution sol = new Solution();
		sol.findLucky(arr1);
	}
}