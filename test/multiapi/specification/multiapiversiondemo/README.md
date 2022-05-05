# Testing MultiapiDemo

### Tag: v1

These settings apply only when `--tag=v1` is specified on the command line.

``` yaml $(tag) == 'v1'
input-file: ../../../../node_modules/@microsoft.azure/autorest.testserver/swagger/version-demo1.json
namespace: multiapidemo.v1
output-folder: $(python-sdks-folder)/multiapi/Expected/AcceptanceTests/MultiapiDemo/multiapidemo/v1
```

``` yaml $(tag) == 'v2'
input-file: ../../../../node_modules/@microsoft.azure/autorest.testserver/swagger/version-demo2.json
namespace: multiapidemo.v2
output-folder: $(python-sdks-folder)/multiapi/Expected/AcceptanceTests/MultiapiDemo/multiapidemo/v2
```

### Settings
``` yaml
package-name: multiapidemo
no-namespace-folders: true
license-header: MICROSOFT_MIT_NO_VERSION
```

``` yaml $(multiapi)
clear-output-folder: true
batch:
    - tag: v1
    - tag: v2
    - multiapiscript: true
```

### Multi-api script

``` yaml $(multiapiscript)
output-folder: $(python-sdks-folder)/multiapi/Expected/AcceptanceTests/MultiapiDemo/multiapidemo/
perform-load: false
```
