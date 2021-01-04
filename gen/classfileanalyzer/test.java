/*  Java boolean Array Example
    Save with file name BooleanArray.java   */
   
public class test
{
  public static void main(String args[])
  {
    //BOOLEAN ARRAY DECLARATION
    boolean array[];
    //MEMORY ALLOCATION FOR BOOLEAN ARRAY
    array = new boolean[4];
    //ASSIGNING ELEMENTS TO BOOLEAN ARRAY
    array[0] = true;
    array[1] = false;
    array[2] = false;
    array[3] = false;
    //BOOLEAN ARRAY OUTPUT
    System.out.println("Java boolean Array Example");
    for(int i=0;i<array.length;i++)
    {
      System.out.println("boolean array Element at : "+ i + " " + array[i]);
    }
  }
}