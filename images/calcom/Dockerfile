# Public upstream release, pinned independently of the wrapper tag.
FROM calcom/cal.com:v5.9.1@sha256:ed4509ccbe7409636cb62d25d07f4a624409f797d1cbf07a051e1049652ccfd3
USER 0
# The upstream entrypoint replaces the public URL in these build artifacts.
# Only those targets need to be writable by the runtime user.
RUN chown -R 1000:1000 /calcom/apps/web/.next /calcom/apps/web/public
COPY --chmod=0555 start.sh /usr/local/bin/hakopod-calcom-start
USER 1000:1000
ENV HOME=/tmp
WORKDIR /calcom
CMD ["/usr/local/bin/hakopod-calcom-start"]
