import requests

def query(string):
    output=list()
    user_agent={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:32.0) Gecko/20100101 Firefox/32.0"}
    res=requests.get("https://viewdns.info/reversewhois/?q="+string,headers = user_agent)
    try:
        first_prase=res.text.split('These are listed below:<br><br><table border="1">')[1].split('</table>')[0].split('<tr>')[1:]
        for i in first_prase:
            a_data=list()
            a_data.append(i.split('<td>')[1].split('</td>')[0])
            a_data.append(i.split('<td>')[2].split('</td>')[0])
            a_data.append(i.split('<td>')[-1].split('</td>')[0])
            output.append(a_data)
        return output
    except:
        return None
if __name__=="__main__":
    string=input("Enter the email or name or company:")
    data=query(string)
    print("result for "+string+" :\n")
    if data==None:
        print("    No result!")
        exit(0)
    for i in data:
        print(" - domain : "+i[0])
        print("    registrar : "+i[2])
        print("    created_date : "+i[1])
        print()
