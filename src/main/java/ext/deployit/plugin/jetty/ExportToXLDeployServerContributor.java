/**
 * THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
 * FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
 */
package ext.deployit.plugin.jetty;

import com.xebialabs.deployit.plugin.api.deployment.planning.Contributor;
import com.xebialabs.deployit.plugin.api.deployment.planning.DeploymentPlanningContext;
import com.xebialabs.deployit.plugin.api.deployment.specification.Delta;
import com.xebialabs.deployit.plugin.api.deployment.specification.Deltas;
import com.xebialabs.deployit.plugin.api.deployment.specification.Operation;
import com.xebialabs.deployit.plugin.api.reflect.Type;

public class ExportToXLDeployServerContributor {

	@Contributor
	static public void exportDarAndPushToServer(Deltas deltas, DeploymentPlanningContext ctx) {
		for (Delta delta : deltas.getDeltas()) {
			if (delta.getOperation() == Operation.DESTROY) {
				if (Type.valueOf("jetty.DeployedDarPackage").equals(delta.getPrevious().getType())
					 && Type.valueOf("jetty.Server").equals(delta.getPrevious().getContainer().getType())) {
					ctx.addStep(new RemoveDarFromServerStep(delta.getPrevious()));
				}
			}
		}
	}

}