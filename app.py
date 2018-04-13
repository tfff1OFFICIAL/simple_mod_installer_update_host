import falcon


class VersionDataResource(object):
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = ('{"1.0": "https://s3-ap-southeast-2.amazonaws.com/tfff1-data/simple+mod+installer/simple.mod.installer.v3.0.4.msi"}')


app = falcon.API()

versions = VersionDataResource()

app.add_route("/versions.json", versions)
