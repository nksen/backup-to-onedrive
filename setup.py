"""
--Naim Sen--
opens onedrive link and saves the session

"""

import onedrivesdk

def authenticate():
    import onedrivesdk
    from onedrivesdk.helpers import GetAuthCodeServer
   
    redirect_uri = 'http://localhost:5000/login/authorized'
    client_secret = 'leyOGUMS23}ulglTR392(;?'
    scopes = ['wl.signin', 'wl.offline_access', 'onedrive.readwrite']

    client = onedrivesdk.get_default_client(
        client_id='325892db-391d-4ac1-bbd2-86f6f085f105', scopes=scopes)
    
    auth_url = client.auth_provider.get_auth_url(redirect_uri)
    
    # this will block until we have the code
    code = GetAuthCodeServer.get_auth_code(auth_url, redirect_uri)

    client.auth_provider.authenticate(code, redirect_uri, client_secret)
    print("Success")
    return client

if __name__ == '__main__':
    authenticate()
