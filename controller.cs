using UnityEngine;

public class controller : MonoBehaviour
{
    public UDPReceive udpReceive;
    public GameObject[] handpoints;
    // Start is called once before the first execution of Update after the MonoBehaviour is created
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        string data=udpReceive.data;
        data=data.Remove(data.Length-1,1);
        data=data.Remove(0,1);
        string[] point=data.Split(',');
        print(point[0]);

        for(int i=0;i<21;i++){
            float x=5-float.Parse(point[i*3])/100;
            float y= float.Parse(point[i*3+1])/100;   
            float z= float.Parse(point[i*3+2])/100;

            handpoints[i].transform.localPosition=new Vector3(x,y,z);
        }
    }
}
