DESTROY_RESOURCES = 40
CREATE_RESOURCES = 60


def apply_changelog_steps(d, ctx):
    step = steps.jython(description="Apply changelog [%s] in jetty [%s]" % (d.name, d.container.name),
                        order=CREATE_RESOURCES,
                        script='jetty/apply_changelog.py',
                        jython_context={"container": d.container, "deployed": d})
    ctx.addStep(step)
    step = steps.jython(description="Create deployment rollback tag [v%s] in jetty [%s]" % (d.rollbackVersion, d.container.name),
                        order=CREATE_RESOURCES,
                        script='jetty/apply_tag.py',
                        jython_context={"container": d.container, "tag": "v%s" % d.rollbackVersion})
    ctx.addStep(step)


def handle_create(d, ctx):
    step = steps.jython(description="Create initial deployment rollback tag [%s] in jetty [%s]" % (d.baseRollbackTag, d.container.name),
                        order=CREATE_RESOURCES,
                        script='jetty/apply_tag.py',
                        jython_context={"container": d.container, "tag": d.baseRollbackTag})
    ctx.addStep(step)
    apply_changelog_steps(d, ctx)


def handle_destroy(d, ctx):
    step = steps.jython(description="Rollback to tag [%s] in jetty [%s]" % (d.baseRollbackTag, d.container.name),
                        order=DESTROY_RESOURCES,
                        script='jetty/apply_rollback.py',
                        jython_context={"container": d.container, "tag": d.baseRollbackTag, "deployed": d})
    ctx.addStep(step)

def handle_modify(pd, d, ctx):
    if d.rollbackVersion < pd.rollbackVersion:
        step = steps.jython(description="Rollback to tag [v%s] in jetty [%s]" % (d.rollbackVersion, d.container.name),
                            order=DESTROY_RESOURCES,
                            script='jetty/apply_rollback.py',
                            jython_context={"container": d.container, "tag": "v%s" % d.rollbackVersion, "deployed": pd})
        ctx.addStep(step)
    else:
        apply_changelog_steps(d, ctx)


operation = str(delta.operation)

if operation == "CREATE":
    handle_create(deployed, context)
elif operation == "DESTROY":
    handle_destroy(previousDeployed, context)
elif operation == "MODIFY":
    handle_modify(previousDeployed, deployed, context)

