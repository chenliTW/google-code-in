import requests
api_key=""

if __name__=="__main__":
    query=input("Enter the email or name or company:")
    res=requests.get("https://api.viewdns.info/reversewhois/?q="+query+"&apikey="+api_key+"&output=json")
    data=res.json()
    print("result for "+query+" :\n")
    for i in data["response"]["matches"]:
        print(" - domain : "+i["domain"])
        print("    registrar : "+i["registrar"])
        print("    created_date : "+i["created_date"])
        print()
