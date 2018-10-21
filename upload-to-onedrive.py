"""
--Naim Sen--
Uploads the tarball backup to onedrive
"""

import onedrivesdk

def authenticate_app():
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

def authenticate_app_2():
    redirect_uri = 'http://localhost:5000/login/authorized'
    client_secret = 'leyOGUMS23}ulglTR392(;?'
    client_id = '325892db-391d-4ac1-bbd2-86f6f085f105'
    api_base_url = 'https://api.onedrive.com/v1.0/'
    scopes = ['wl.signin', 'wl.offline_access', 'onedrive.readwrite']
    
    http_provider = onedrivesdk.HttpProvider()
    auth_provider = onedrivesdk.AuthProvider(
        http_provider=http_provider,
        client_id=client_id,
        scopes=scopes)
    
    client = onedrivesdk.OneDriveClient(api_base_url, auth_provider, http_provider)
    auth_url = client.auth_provider.get_auth_url(redirect_uri)
    # Ask for the code
    print('Paste this URL into your browser, approve the app\'s access.')
    print('Copy everything in the address bar after "code=", and paste it below.')
    print(auth_url)
    code = input('Paste code here: ')

    
if __name__ == "__main__":
    authenticate_app()
