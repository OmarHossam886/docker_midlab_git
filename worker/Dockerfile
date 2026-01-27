FROM --platform=${BUILDPLATFORM} mcr.microsoft.com/dotnet/sdk:7.0 AS build
ARG TARGETPLATFORM
ARG TARGETARCH
ARG BUILDPLATFORM
RUN echo "I am running on $BUILDPLATFORM, building for $TARGETPLATFORM"

WORKDIR /docker_midlab/worker
COPY . .

RUN dotnet clean
RUN dotnet restore -r linux-x64
RUN dotnet publish -c release -o /out -r linux-x64 --self-contained false --no-restore

# app image
FROM mcr.microsoft.com/dotnet/runtime:7.0
WORKDIR /docker_midlab/worker
COPY --from=build /out .
ENTRYPOINT ["dotnet", "Worker.dll"]